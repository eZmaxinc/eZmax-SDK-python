# CustomDocumenttypechecklistResponse

Generic Documenttypechecklist Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_documenttypechecklist_id** | **int** | The unique ID of the Documenttypechecklist | 
**fki_documenttype_id** | **int** | The unique ID of the Documenttype | [optional] 
**fki_adjustment_id** | **int** | The unique ID of the Adjustment | [optional] 
**fki_agent_id** | **int** | The unique ID of the Agent. | [optional] 
**fki_bankaccount_id** | **int** | The unique ID of the Bankaccount | [optional] 
**fki_broker_id** | **int** | The unique ID of the Broker. | [optional] 
**fki_buyercontract_id** | **int** | The unique ID of the Buyercontract | [optional] 
**fki_commissionadvance_id** | **int** | The unique ID of the Commissionadvance | [optional] 
**fki_communication_id** | **int** | The unique ID of the Communication. | [optional] 
**fki_customer_id** | **int** | The unique ID of the Customer. | [optional] 
**fki_customertemplate_id** | **int** | The unique ID of the Customertemplate | [optional] 
**fki_deposit_id** | **int** | The unique ID of the Deposit | [optional] 
**fki_deposittransitcheque_id** | **int** | The unique ID of the Deposittransitcheque | [optional] 
**fki_disclosure_id** | **int** | The unique ID of the Disclosure | [optional] 
**fki_electronicfundstransfer_id** | **int** | The unique ID of the Electronicfundstransfer | [optional] 
**fki_employee_id** | **int** | The unique ID of the Employee. | [optional] 
**fki_externalbroker_id** | **int** | The unique ID of the Externalbroker. | [optional] 
**fki_ezsignfolder_id** | **int** | The unique ID of the Ezsignfolder | [optional] 
**fki_folder_id** | **int** | The unique ID of the Folder | [optional] 
**fki_inscription_id** | **int** | The unique ID of the Inscription. | [optional] 
**fki_inscriptionnotauthenticated_id** | **int** | The unique ID of the Inscriptionnotauthenticated. | [optional] 
**fki_inscriptiontemp_id** | **int** | The unique ID of the Inscriptiontemp | [optional] 
**fki_invoice_id** | **int** | The unique ID of the Invoice. | [optional] 
**fki_lead_id** | **int** | The unique ID of the Lead | [optional] 
**fki_notary_id** | **int** | The unique ID of the Notary. | [optional] 
**fki_officetaxreport_id** | **int** | The unique ID of the Officetaxreport | [optional] 
**fki_otherincome_id** | **int** | The unique ID of the Otherincome | [optional] 
**fki_paymentpreparation_id** | **int** | The unique ID of the Paymentpreparation | [optional] 
**fki_purchase_id** | **int** | The unique ID of the Purchase | [optional] 
**fki_reconciliation_id** | **int** | The unique ID of the Reconciliation | [optional] 
**fki_rejectedoffertopurchase_id** | **int** | The unique ID of the Rejectedoffertopurchase | [optional] 
**fki_salary_id** | **int** | The unique ID of the Salary | [optional] 
**fki_supplier_id** | **int** | The unique ID of the Supplier. | [optional] 
**fki_tranqcontract_id** | **int** | The unique ID of the Tranqcontract | [optional] 
**e_documenttypechecklist_status** | [**FieldEDocumenttypechecklistStatus**](FieldEDocumenttypechecklistStatus.md) |  | 
**t_documenttypechecklist_comment** | **str** | The comment of the Documenttypechecklist | [optional] 

## Example

```python
from eZmaxApi.models.custom_documenttypechecklist_response import CustomDocumenttypechecklistResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomDocumenttypechecklistResponse from a JSON string
custom_documenttypechecklist_response_instance = CustomDocumenttypechecklistResponse.from_json(json)
# print the JSON string representation of the object
print(CustomDocumenttypechecklistResponse.to_json())

# convert the object into a dict
custom_documenttypechecklist_response_dict = custom_documenttypechecklist_response_instance.to_dict()
# create an instance of CustomDocumenttypechecklistResponse from a dict
custom_documenttypechecklist_response_from_dict = CustomDocumenttypechecklistResponse.from_dict(custom_documenttypechecklist_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


