# EzmaxpartnerResponse

An Ezmaxpartner Object

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
from eZmaxApi.models.ezmaxpartner_response import EzmaxpartnerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EzmaxpartnerResponse from a JSON string
ezmaxpartner_response_instance = EzmaxpartnerResponse.from_json(json)
# print the JSON string representation of the object
print(EzmaxpartnerResponse.to_json())

# convert the object into a dict
ezmaxpartner_response_dict = ezmaxpartner_response_instance.to_dict()
# create an instance of EzmaxpartnerResponse from a dict
ezmaxpartner_response_from_dict = EzmaxpartnerResponse.from_dict(ezmaxpartner_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


