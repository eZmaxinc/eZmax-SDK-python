# EzmaxpartnerproductstageResponseCompound

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
from eZmaxApi.models.ezmaxpartnerproductstage_response_compound import EzmaxpartnerproductstageResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of EzmaxpartnerproductstageResponseCompound from a JSON string
ezmaxpartnerproductstage_response_compound_instance = EzmaxpartnerproductstageResponseCompound.from_json(json)
# print the JSON string representation of the object
print(EzmaxpartnerproductstageResponseCompound.to_json())

# convert the object into a dict
ezmaxpartnerproductstage_response_compound_dict = ezmaxpartnerproductstage_response_compound_instance.to_dict()
# create an instance of EzmaxpartnerproductstageResponseCompound from a dict
ezmaxpartnerproductstage_response_compound_from_dict = EzmaxpartnerproductstageResponseCompound.from_dict(ezmaxpartnerproductstage_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


