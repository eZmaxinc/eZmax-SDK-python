# EzmaxpartnerproductstagesubscriptionResponse

A Ezmaxpartnerproductstagesubscription-Response Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezmaxpartnerproductstagesubscription_id** | **int** | The unique ID of the Ezmaxpartnerproductstagesubscription | 
**fki_ezmaxpartnerproductstage_id** | **int** | The unique ID of the Ezmaxpartnerproductstage | 
**b_ezmaxpartnerproductstagesubscription_isinstalled** | **bool** | Whether the Ezmaxpartnerproductstagesubscription is installed or not | 
**obj_audit** | [**CommonAudit**](CommonAudit.md) |  | 

## Example

```python
from eZmaxApi.models.ezmaxpartnerproductstagesubscription_response import EzmaxpartnerproductstagesubscriptionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EzmaxpartnerproductstagesubscriptionResponse from a JSON string
ezmaxpartnerproductstagesubscription_response_instance = EzmaxpartnerproductstagesubscriptionResponse.from_json(json)
# print the JSON string representation of the object
print(EzmaxpartnerproductstagesubscriptionResponse.to_json())

# convert the object into a dict
ezmaxpartnerproductstagesubscription_response_dict = ezmaxpartnerproductstagesubscription_response_instance.to_dict()
# create an instance of EzmaxpartnerproductstagesubscriptionResponse from a dict
ezmaxpartnerproductstagesubscription_response_from_dict = EzmaxpartnerproductstagesubscriptionResponse.from_dict(ezmaxpartnerproductstagesubscription_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


