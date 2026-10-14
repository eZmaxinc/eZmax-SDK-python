# ElectronicfundstransferListElement

A Electronicfundstransfer List Element

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_electronicfundstransfer_id** | **int** | The unique ID of the Electronicfundstransfer | 
**fki_paymentmethod_id** | **int** | The unique ID of the Paymentmethod | 
**fki_user_id_created** | **int** | The unique ID of the User | [optional] 
**s_paymentmethod_description_x** | **str** | The description of the Paymentmethod in the language of the requester | [optional] 
**s_user_loginname_created** | **str** | The login name of the User. | [optional] 
**i_electronicfundstransfer_number** | **int** | The number of the Electronicfundstransfer | 
**dt_electronicfundstransfer_date** | **str** | The date of the Electronicfundstransfer | 
**i_electronicfundstransfer_transactioncount** | **int** | The count of transactions in this Electronicfundstransfer. | [optional] 
**d_electronicfundstransfer_amountvisible** | **str** | The sum of Electronicfundstransfertransaction we can consult. This sum can be different than total amount. | [optional] 

## Example

```python
from eZmaxApi.models.electronicfundstransfer_list_element import ElectronicfundstransferListElement

# TODO update the JSON string below
json = "{}"
# create an instance of ElectronicfundstransferListElement from a JSON string
electronicfundstransfer_list_element_instance = ElectronicfundstransferListElement.from_json(json)
# print the JSON string representation of the object
print(ElectronicfundstransferListElement.to_json())

# convert the object into a dict
electronicfundstransfer_list_element_dict = electronicfundstransfer_list_element_instance.to_dict()
# create an instance of ElectronicfundstransferListElement from a dict
electronicfundstransfer_list_element_from_dict = ElectronicfundstransferListElement.from_dict(electronicfundstransfer_list_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


