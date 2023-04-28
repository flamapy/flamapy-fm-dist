import os
from flask import Blueprint, request, jsonify
from operations.info import get_plugins, get_operations

info_bp = Blueprint('info_bp', __name__, url_prefix='/api/v1/info')


@info_bp.route('/plugins', methods=['GET'])
def info_plugins():
    # Get plugins
    plugins = get_plugins()

    # Return result
    if (plugins):
        return jsonify(plugins)
    else:
        return jsonify(error='No plugins found'), 404


@info_bp.route('/<string:plugin>/operations/', methods=['GET'])
def info_operations(plugin: str):
    # Get operations
    operations = get_operations(plugin)

    # Return result
    if operations:
        return jsonify(operations), 200
    else:
        return jsonify(error='No operations found'), 404
