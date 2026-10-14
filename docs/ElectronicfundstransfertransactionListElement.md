# ElectronicfundstransfertransactionListElement

A Electronicfundstransfertransaction List Element

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_electronicfundstransfertransaction_id** | **int** | The unique ID of the Electronicfundstransfertransaction | 
**i_electronicfundstransfer_number** | **int** | The number of the Electronicfundstransfer | [optional] 
**d_electronicfundstransfertransaction_amount** | **str** | The amount of the Electronicfundstransfertransaction | 
**dt_electronicfundstransfertransaction_date** | **str** | The date of the Electronicfundstransfertransaction | 

## Example

```python
from eZmaxApi.models.electronicfundstransfertransaction_list_element import ElectronicfundstransfertransactionListElement

# TODO update the JSON string below
json = "{}"
# create an instance of ElectronicfundstransfertransactionListElement from a JSON string
electronicfundstransfertransaction_list_element_instance = ElectronicfundstransfertransactionListElement.from_json(json)
# print the JSON string representation of the object
print(ElectronicfundstransfertransactionListElement.to_json())

# convert the object into a dict
electronicfundstransfertransaction_list_element_dict = electronicfundstransfertransaction_list_element_instance.to_dict()
# create an instance of ElectronicfundstransfertransactionListElement from a dict
electronicfundstransfertransaction_list_element_from_dict = ElectronicfundstransfertransactionListElement.from_dict(electronicfundstransfertransaction_list_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


