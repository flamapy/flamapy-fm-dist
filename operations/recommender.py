import os
import csv

from typing import NewType
from flamapy.core.discover import DiscoverMetamodels


def check_recommendation_objects(model, products, query):
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

        os.remove(query_csvconf)
        return recommendations
    except:
        os.remove(query_csvconf)
        print("No product recommendations found.")
