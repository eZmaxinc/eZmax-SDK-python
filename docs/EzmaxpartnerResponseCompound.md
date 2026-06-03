# EzmaxpartnerResponseCompound

Payload for GET /1/object/activesession/getCurrent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**e_ezmaxpartner_customdevelopment** | [**FieldEEzmaxpartnerCustomdevelopment**](FieldEEzmaxpartnerCustomdevelopment.md) |  | 
**obj_ezmaxpartner_address** | [**MultilingualEzmaxpartnerAddress**](MultilingualEzmaxpartnerAddress.md) |  | 
**obj_ezmaxpartner_description** | [**MultilingualEzmaxpartnerDescription**](MultilingualEzmaxpartnerDescription.md) |  | 
**obj_ezmaxpartner_emailaddress** | [**MultilingualEzmaxpartnerEmailaddress**](MultilingualEzmaxpartnerEmailaddress.md) |  | 
**obj_ezmaxpartner_name** | [**MultilingualEzmaxpartnerName**](MultilingualEzmaxpartnerName.md) |  | 
**obj_ezmaxpartner_phone_e164** | [**MultilingualEzmaxpartnerPhoneE164**](MultilingualEzmaxpartnerPhoneE164.md) |  | 
**obj_ezmaxpartner_shortdescription** | [**MultilingualEzmaxpartnerShortdescription**](MultilingualEzmaxpartnerShortdescription.md) |  | 
**obj_ezmaxpartner_url** | [**MultilingualEzmaxpartnerUrl**](MultilingualEzmaxpartnerUrl.md) |  | 
**b_ezmaxpartner_isactive** | **bool** | Whether the Ezmaxpartner is active or not | [optional] 

## Example

```python
from eZmaxApi.models.ezmaxpartner_response_compound import EzmaxpartnerResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of EzmaxpartnerResponseCompound from a JSON string
ezmaxpartner_response_compound_instance = EzmaxpartnerResponseCompound.from_json(json)
# print the JSON string representation of the object
print(EzmaxpartnerResponseCompound.to_json())

# convert the object into a dict
ezmaxpartner_response_compound_dict = ezmaxpartner_response_compound_instance.to_dict()
# create an instance of EzmaxpartnerResponseCompound from a dict
ezmaxpartner_response_compound_from_dict = EzmaxpartnerResponseCompound.from_dict(ezmaxpartner_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


