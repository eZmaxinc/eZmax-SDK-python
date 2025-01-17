# EzmaxinvoicinguserResponseCompound

A Ezmaxinvoicinguser Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_contact_name** | [**CustomContactNameResponse**](CustomContactNameResponse.md) |  | 

## Example

```python
from eZmaxApi.models.ezmaxinvoicinguser_response_compound import EzmaxinvoicinguserResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of EzmaxinvoicinguserResponseCompound from a JSON string
ezmaxinvoicinguser_response_compound_instance = EzmaxinvoicinguserResponseCompound.from_json(json)
# print the JSON string representation of the object
print(EzmaxinvoicinguserResponseCompound.to_json())

# convert the object into a dict
ezmaxinvoicinguser_response_compound_dict = ezmaxinvoicinguser_response_compound_instance.to_dict()
# create an instance of EzmaxinvoicinguserResponseCompound from a dict
ezmaxinvoicinguser_response_compound_from_dict = EzmaxinvoicinguserResponseCompound.from_dict(ezmaxinvoicinguser_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


