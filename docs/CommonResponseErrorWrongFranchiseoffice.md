# CommonResponseErrorWrongFranchiseoffice

Error Message when a Franchisebroker is not in this Franchiseoffice.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_error_message** | **str** | The message giving details about the error | 
**e_error_code** | [**FieldEErrorCode**](FieldEErrorCode.md) |  | 
**a_s_error_messagedetail** | **List[str]** | More error message detail | [optional] 
**fki_franchiseagence_id** | **int** | The unique ID of the Franchiseagence | 
**s_franchiseagence_name** | **str** | The name of the Franchiseagence | 
**fki_franchiseoffice_id** | **int** | The unique ID of the Franchisereoffice | 
**i_franchiseoffice_code** | **str** | The code of the Franchiseoffice | 

## Example

```python
from eZmaxApi.models.common_response_error_wrong_franchiseoffice import CommonResponseErrorWrongFranchiseoffice

# TODO update the JSON string below
json = "{}"
# create an instance of CommonResponseErrorWrongFranchiseoffice from a JSON string
common_response_error_wrong_franchiseoffice_instance = CommonResponseErrorWrongFranchiseoffice.from_json(json)
# print the JSON string representation of the object
print(CommonResponseErrorWrongFranchiseoffice.to_json())

# convert the object into a dict
common_response_error_wrong_franchiseoffice_dict = common_response_error_wrong_franchiseoffice_instance.to_dict()
# create an instance of CommonResponseErrorWrongFranchiseoffice from a dict
common_response_error_wrong_franchiseoffice_from_dict = CommonResponseErrorWrongFranchiseoffice.from_dict(common_response_error_wrong_franchiseoffice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


