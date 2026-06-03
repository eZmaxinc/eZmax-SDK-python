# MultilingualEzmaxpartnerAddress

Address of the Ezmaxpartner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_ezmaxpartner_address1** | **str** | The complete address in a single line | [optional] 
**s_ezmaxpartner_address2** | **str** | The complete address in a single line | [optional] 

## Example

```python
from eZmaxApi.models.multilingual_ezmaxpartner_address import MultilingualEzmaxpartnerAddress

# TODO update the JSON string below
json = "{}"
# create an instance of MultilingualEzmaxpartnerAddress from a JSON string
multilingual_ezmaxpartner_address_instance = MultilingualEzmaxpartnerAddress.from_json(json)
# print the JSON string representation of the object
print(MultilingualEzmaxpartnerAddress.to_json())

# convert the object into a dict
multilingual_ezmaxpartner_address_dict = multilingual_ezmaxpartner_address_instance.to_dict()
# create an instance of MultilingualEzmaxpartnerAddress from a dict
multilingual_ezmaxpartner_address_from_dict = MultilingualEzmaxpartnerAddress.from_dict(multilingual_ezmaxpartner_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


