import os
import csv

from typing import NewType
from flamapy.core.discover import DiscoverMetamodels


def check_recommendation_objects(model, products, query=None):
    """
    Check if the objects are valid for the recommendation operation.
    :param model: The model file.
    :param products: The products file.
    :param query: The query file.
    :return: 1 if the objects are valid, an error message otherwise.
    """

    dm = DiscoverMetamodels()
    try:
        fm = dm.use_transformation_t2m(model, "fm")
        features = [feature.name for feature in fm.get_features()]
    except:
        error = "The model does not exist or is not a valid feature model."
        return error

    try:
        with open(products, newline='') as csvfile:
            csv_reader = csv.reader(csvfile)
            assortment_dict = {rows[0].replace("product=", ""): [i.replace("=", "").replace("false", "").replace("true", "") for i in rows[1:] if
                                                                 '=' in i] for rows in csv_reader}
            for value in assortment_dict.values():
                value.sort()
            for configuration_object in assortment_dict.values():
                for feature in configuration_object:
                    if feature not in features:
                        error = "The product file does not match the model."
                        return error
    except:
        error = "The product file does not exist or is not a valid csv file."
        return error

    if query is not None:
        try:
            query_features = []
            with open(query, newline='') as csvfile:
                csv_reader = csv.reader(csvfile)
                for row in csv_reader:
                    if row[1]:
                        query_features.append(row[0])

            for feature in query_features:
                if feature not in features:
                    error = "The query file does not match the model."
                    return error
        except:
            error = "The query file does not exist or is not a valid csv file."
            return error

    return 1


def get_recommendations(model, products, query):
    """
    Get recommendations for a given query.
    :param model: The model file.
    :param products: The products file.
    :param query: The query file.
    :return: A dictionary with the recommendations.
    """

    dm = DiscoverMetamodels()

    message = check_recommendation_objects(model, products, query)
    if message != 1:
        return message

    query_csvconf = query.replace('.csv', '.csvconf')

    with open(query_csvconf, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        with open(query, newline='') as original_csvfile:
            csv_reader = csv.reader(original_csvfile)
            for row in csv_reader:
                csv_writer.writerow(row)

    try:
        configurations = dm.use_operation_from_file(
            "Filter", model, configuration_file=query_csvconf)

        configurations = {i: configuration for i,
                          configuration in enumerate(configurations)}
        for value in configurations.values():
            value.sort()

        with open(products, newline='') as csvfile:
            csv_reader = csv.reader(csvfile)
            products = {rows[0].replace("product=", ""): [i.replace("=true", "") for i in rows[1:] if
                                                          '=true' in i] for rows in csv_reader}
            for value in products.values():
                value.sort()

        recommendations = {}
        for configuration in configurations.values():
            for product, features in products.items():
                if configuration == features:
                    recommendations[product] = configuration

        recommendations = dict(
            sorted(recommendations.items(), key=lambda item: len(item[1]), reverse=True))

        os.remove(query_csvconf)
        return recommendations
    except:
        os.remove(query_csvconf)
        print("No product recommendations found.")


def consistent_configurations(model, products):
    dm = DiscoverMetamodels()

    message = check_recommendation_objects(model, products)
    if message != 1:
        return message

    try:
        configurations = dm.use_operation_from_file('Products', model)
        configurations = {i: configuration for i,
                          configuration in enumerate(configurations)}
        for value in configurations.values():
            value.sort()

        with open(products, newline='') as csvfile:
            csv_reader = csv.reader(csvfile)
            products = {rows[0].replace("product=", ""): [i.replace("=true", "") for i in rows[1:] if
                                                          '=true' in i] for rows in csv_reader}
            for value in products.values():
                value.sort()

        consistent_products = {}
        for configuration in configurations.values():
            for product, features in products.items():
                if configuration == features:
                    consistent_products[product] = configuration

        consistent_products = dict(sorted(
            consistent_products.items(), key=lambda item: len(item[1]), reverse=True))

        return products, consistent_products
    except:
        print("No consistent configurations found.")


def restrictiveness(model, products, feature_list):
    products, consistent_products = consistent_configurations(model, products)

    valid_products = {}
    for product, features in consistent_products.items():
        if all(feature in features for feature in feature_list):
            valid_products[product] = features

    return len(valid_products) / len(products) * 100
