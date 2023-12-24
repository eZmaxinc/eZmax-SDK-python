# MultilingualPaymenttermDescription

Description of the Paymentterm

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_paymentterm_description1** | **str** | The description of the Paymentterm in French | [optional] 
**s_paymentterm_description2** | **str** | The description of the Paymentterm in English | [optional] 

## Example

```python
from eZmaxApi.models.multilingual_paymentterm_description import MultilingualPaymenttermDescription

# TODO update the JSON string below
json = "{}"
# create an instance of MultilingualPaymenttermDescription from a JSON string
multilingual_paymentterm_description_instance = MultilingualPaymenttermDescription.from_json(json)
# print the JSON string representation of the object
print MultilingualPaymenttermDescription.to_json()

# convert the object into a dict
multilingual_paymentterm_description_dict = multilingual_paymentterm_description_instance.to_dict()
# create an instance of MultilingualPaymenttermDescription from a dict
multilingual_paymentterm_description_form_dict = multilingual_paymentterm_description.from_dict(multilingual_paymentterm_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


