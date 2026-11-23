# EzmaxpartnerproductstageResponse

A Ezmaxpartnerproductstage Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezmaxpartnerproductstage_id** | **int** | The unique ID of the Ezmaxpartnerproductstage | 
**fki_ezmaxpartnerproduct_id** | **int** | The unique ID of the Ezmaxpartnerproduct | 
**e_ezmaxpartnerproductstage_code** | [**FieldEEzmaxpartnerproductstageCode**](FieldEEzmaxpartnerproductstageCode.md) |  | 
**e_ezmaxpartnerproductstage_installationtype** | [**FieldEEzmaxpartnerproductstageInstallationtype**](FieldEEzmaxpartnerproductstageInstallationtype.md) |  | 
**b_ezmaxpartnerproductstage_published** | **bool** | Whether the Ezmaxpartnerproducstage is published or not | 
**b_ezmaxpartnerproductstage_installed** | **bool** | Whether the Ezmaxpartnerproductstage is installed or not | 
**obj_ezmaxpartnerproductstagesubscription** | [**EzmaxpartnerproductstagesubscriptionResponse**](EzmaxpartnerproductstagesubscriptionResponse.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezmaxpartnerproductstage_response import EzmaxpartnerproductstageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EzmaxpartnerproductstageResponse from a JSON string
ezmaxpartnerproductstage_response_instance = EzmaxpartnerproductstageResponse.from_json(json)
# print the JSON string representation of the object
print(EzmaxpartnerproductstageResponse.to_json())

# convert the object into a dict
ezmaxpartnerproductstage_response_dict = ezmaxpartnerproductstage_response_instance.to_dict()
# create an instance of EzmaxpartnerproductstageResponse from a dict
ezmaxpartnerproductstage_response_from_dict = EzmaxpartnerproductstageResponse.from_dict(ezmaxpartnerproductstage_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


