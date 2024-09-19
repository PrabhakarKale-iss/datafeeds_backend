# routes/client_company.py
from flask import Blueprint, jsonify, request, current_app

client_company_bp = Blueprint('client_company', __name__)

@client_company_bp.route('', methods=['POST'])
def create_company():
    data = request.get_json()
    company_name = data.get('company_name')
    datafeed_status = data.get('datafeed_status')
    uses_id = data.get('uses_id')

    if not company_name or not datafeed_status:
        return jsonify({'error': 'Company name and datafeed status are required'}), 400

    db_manager = current_app.extensions['db_manager']
    query = "INSERT INTO client_company (company_name, datafeed_status, uses_id) VALUES (%s, %s, %s)"
    db_manager.execute_query(query, (company_name, datafeed_status, uses_id))
    return jsonify({'message': 'Client company created successfully'}), 201

@client_company_bp.route('', methods=['GET'])
def get_companies():
    db_manager = current_app.extensions['db_manager']
    query = "SELECT * FROM client_company"
    companies = db_manager.fetch_data_to_json(query)
    return companies

@client_company_bp.route('/<int:company_id>', methods=['GET'])
def get_company(company_id):
    db_manager = current_app.extensions['db_manager']
    query = "SELECT * FROM client_company WHERE company_id = %s"
    company = db_manager.fetch_one(query, (company_id,))
    if company:
        column_names = [i[0] for i in db_manager.cursor.description]
        return jsonify(dict(zip(column_names, company)))
    return jsonify({'error': 'Client company not found'}), 404

@client_company_bp.route('/<int:company_id>', methods=['PUT'])
def update_company(company_id):
    data = request.get_json()
    company_name = data.get('company_name')
    datafeed_status = data.get('datafeed_status')
    uses_id = data.get('uses_id')

    if not company_name or not datafeed_status:
        return jsonify({'error': 'Company name and datafeed status are required'}), 400

    db_manager = current_app.extensions['db_manager']
    query = "UPDATE client_company SET company_name = %s, datafeed_status = %s, uses_id = %s WHERE company_id = %s"
    result = db_manager.execute_query(query, (company_name, datafeed_status, uses_id, company_id))
    if result:
        return jsonify({'message': 'Client company updated successfully'})
    return jsonify({'error': 'Client company not found'}), 404

@client_company_bp.route('/<int:company_id>', methods=['DELETE'])
def delete_company(company_id):
    db_manager = current_app.extensions['db_manager']
    query = "DELETE FROM client_company WHERE company_id = %s"
    result = db_manager.execute_query(query, (company_id,))
    if result:
        return jsonify({'message': 'Client company deleted successfully'})
    return jsonify({'error': 'Client company not found'}), 404
