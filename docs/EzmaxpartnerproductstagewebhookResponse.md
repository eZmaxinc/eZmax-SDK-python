# EzmaxpartnerproductstagewebhookResponse

A Ezmaxpartnerproductstagewebhook Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezmaxpartnerproductstagewebhook_id** | **int** | The unique ID of the Ezmaxpartnerproductstagewebhook | [optional] 
**fki_ezmaxpartnerproductstage_id** | **int** | The unique ID of the Ezmaxpartnerproductstage | 
**s_ezmaxpartnerproductstage_code** | **str** | The code of the sEzmaxpartnerproductstage | [optional] 
**e_ezmaxpartnerproductstagewebhook_module** | [**FieldEEzmaxpartnerproductstagewebhookModule**](FieldEEzmaxpartnerproductstagewebhookModule.md) |  | 
**e_ezmaxpartnerproductstagewebhook_ezmaxpartnerevent** | [**FieldEEzmaxpartnerproductstagewebhookEzmaxpartnerevent**](FieldEEzmaxpartnerproductstagewebhookEzmaxpartnerevent.md) |  | [optional] 
**e_ezmaxpartnerproductstagewebhook_ezsignevent** | [**FieldEEzmaxpartnerproductstagewebhookEzsignevent**](FieldEEzmaxpartnerproductstagewebhookEzsignevent.md) |  | [optional] 
**e_ezmaxpartnerproductstagewebhook_managementevent** | [**FieldEEzmaxpartnerproductstagewebhookManagementevent**](FieldEEzmaxpartnerproductstagewebhookManagementevent.md) |  | [optional] 
**e_ezmaxpartnerproductstagewebhook_realestateevent** | [**FieldEEzmaxpartnerproductstagewebhookRealestateevent**](FieldEEzmaxpartnerproductstagewebhookRealestateevent.md) |  | [optional] 
**s_ezmaxpartnerproductstagewebhook_description** | **str** | The description of the Ezmaxpartnerproductstagewebhook | [optional] 
**s_ezmaxpartnerproductstagewebhook_url** | **str** | The url of the Ezmaxpartnerproductstagewebhook | [optional] 
**s_ezmaxpartnerproductstagewebhook_emailfailed** | **str** | The emailfailed of the Ezmaxpartnerproductstagewebhook | [optional] 

## Example

```python
from eZmaxApi.models.ezmaxpartnerproductstagewebhook_response import EzmaxpartnerproductstagewebhookResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EzmaxpartnerproductstagewebhookResponse from a JSON string
ezmaxpartnerproductstagewebhook_response_instance = EzmaxpartnerproductstagewebhookResponse.from_json(json)
# print the JSON string representation of the object
print(EzmaxpartnerproductstagewebhookResponse.to_json())

# convert the object into a dict
ezmaxpartnerproductstagewebhook_response_dict = ezmaxpartnerproductstagewebhook_response_instance.to_dict()
# create an instance of EzmaxpartnerproductstagewebhookResponse from a dict
ezmaxpartnerproductstagewebhook_response_from_dict = EzmaxpartnerproductstagewebhookResponse.from_dict(ezmaxpartnerproductstagewebhook_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


