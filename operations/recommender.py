import os
import csv

from typing import NewType
from flamapy.core.discover import DiscoverMetamodels
from itertools import combinations


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
    message = check_recommendation_objects(model, products, query)
    if message != 1:
        return message

    dm = DiscoverMetamodels()

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
    """
    Get the consistent configurations for a given model and products.
    :param model: The model file.
    :param products: The products file.
    :return: A dictionary with the consistent configurations.
    """
    message = check_recommendation_objects(model, products)
    if message != 1:
        return message

    dm = DiscoverMetamodels()

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
    """
    Get the restrictiveness for a given model and products.
    :param model: The model file.
    :param products: The products file.
    :param feature_list: The list of features.
    :return: The restrictiveness.
    """

    message = check_recommendation_objects(model, products)
    if message != 1:
        return message

    products, consistent_products = consistent_configurations(model, products)

    valid_products = {}
    for product, features in consistent_products.items():
        if all(feature in features for feature in feature_list):
            valid_products[product] = features

    return len(valid_products) / len(products) * 100


def accessibility(model, products):
    """
    Get the accessibility for a given model and products.
    :param model: The model file.
    :param products: The products file.
    :return: The accessibility.
    """
    message = check_recommendation_objects(model, products)
    if message != 1:
        return message

    dm = DiscoverMetamodels()

    try:
        fm = dm.use_transformation_t2m(model, "fm")
        features = [feature.name for feature in fm.get_features()
                    if feature.is_leaf()]
    except:
        error = "The model does not exist or is not a valid feature model."
        return error

    try:
        combinations_list = []
        for i in range(1, len(features)+1):
            combos = combinations(features, i)
            for c in combos:
                combinations_list.append(c)
    except:
        error = "Could not generate combinations."
        return error

    try:
        results = {}
        for i in range(1, len(combinations_list)+1):
            query = "./resources/recommender/query.csv"
            with open(query, 'w', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                for feature in combinations_list[i-1]:
                    csv_writer.writerow([feature, "true"])

            result = get_recommendations(model, products, query)
            results[i] = result
            os.remove(query)
    except:
        error = "Could not write query file."
        return error

    results = {key: value for key, value in results.items() if value}

    product_count = {}
    product_keys = []
    with open(products, newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            product_keys.append(row[0].replace("product=", ""))

    for key in product_keys:
        product_count[key] = 0

    for result in results.values():
        for product in result:
            product_count[product] += 1

    return product_count, results


def catalog_coverage(model, products):
    """
    Get the catalog coverage for a given model and products.
    :param model: The model file.
    :param products: The products file.
    :return: The catalog coverage.
    """

    message = check_recommendation_objects(model, products)
    if message != 1:
        return message

    products_count, _ = accessibility(model, products)

    products_with_recommendations = 0
    for product, count in products_count.items():
        if count > 0:
            products_with_recommendations += 1

    coverage = products_with_recommendations / len(products_count) * 100

    if coverage != 100:
        products_without_recommendations = []
        for product, count in products_count.items():
            if count == 0:
                products_without_recommendations.append(product)

        return (coverage, "% - The following products do not have recommendations:",
                products_without_recommendations)
    else:
        return (coverage, "% - All products have recommendations.")


def visibility(model, products, product):
    """
    Get the visibility for a given model and products.
    :param model: The model file.
    :param products: The products file.
    :param product: The product.
    :return: The visibility.
    """

    message = check_recommendation_objects(model, products)
    if message != 1:
        return message

    _, results = accessibility(model, products)
    num = 0
    den = 0
    for key, value in results.items():
        if product in value:
            num += list(value.keys()).index(product) + 1
            den += len(value)

    return (1 - num / den) * 100


def controversy(model, products, feature_list):
    """
    Get the controversy for a given model and products.
    :param model: The model file.
    :param products: The products file.
    :param feature_list: The list of features.
    :return: The controversy.
    """
    message = check_recommendation_objects(model, products)
    if message != 1:
        return message

    dm = DiscoverMetamodels()

    try:
        fm = dm.use_transformation_t2m(model, "fm")
        features = [feature.name for feature in fm.get_features()
                    if feature.is_leaf()]
    except:
        error = "The model does not exist or is not a valid feature model."
        return error

    try:
        combinations_list = []
        for i in range(1, len(features)+1):
            combos = combinations(features, i)
            for c in combos:
                combinations_list.append(c)
    except:
        error = "Could not generate combinations."
        return error

    try:
        results = {}
        for combination in combinations_list:
            query = "./resources/recommender/query.csv"
            with open(query, 'w', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                for feature in combination:
                    csv_writer.writerow([feature, "true"])

            result = get_recommendations(model, products, query)
            results[combination] = result
            os.remove(query)
    except:
        error = "Could not write query file."
        return error

    results = {key: value for key, value in results.items() if not value}

    count = 0
    for key in results.keys():
        if all(feature in key for feature in feature_list):
            count += 1

    return count / len(results) * 100


def global_controversy(model, products):
    """
    Get the global controversy for a given model and products.
    :param model: The model file.
    :param products: The products file.
    :return: The global controversy.
    """

    message = check_recommendation_objects(model, products)
    if message != 1:
        return message

    dm = DiscoverMetamodels()

    try:
        fm = dm.use_transformation_t2m(model, "fm")
        features = [feature.name for feature in fm.get_features()
                    if feature.is_leaf()]
    except:
        error = "The model does not exist or is not a valid feature model."
        return error

    try:
        combinations_list = []
        for i in range(1, len(features)+1):
            combos = combinations(features, i)
            for c in combos:
                combinations_list.append(c)
    except:
        error = "Could not generate combinations."
        return error

    try:
        results = {}
        for combination in combinations_list:
            query = "./resources/recommender/query.csv"
            with open(query, 'w', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                for feature in combination:
                    csv_writer.writerow([feature, "true"])

            result = get_recommendations(model, products, query)
            results[combination] = result
            os.remove(query)
    except:
        error = "Could not write query file."
        return error

    count = 0
    for key, value in results.items():
        if not value:
            count += 1

    return count / len(results) * 100
