# WebsiteRequestCompound

A Website Object and children to create a complete structure

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fki_websitetype_id** | **int** | The unique ID of the Websitetype.  Valid values:  |Value|Description| |-|-| |1|Website| |2|Twitter| |3|Facebook| |4|Survey| | 
**s_website_address** | **str** | The URL of the website. | 

## Example

```python
from eZmaxApi.models.website_request_compound import WebsiteRequestCompound

# TODO update the JSON string below
json = "{}"
# create an instance of WebsiteRequestCompound from a JSON string
website_request_compound_instance = WebsiteRequestCompound.from_json(json)
# print the JSON string representation of the object
print(WebsiteRequestCompound.to_json())

# convert the object into a dict
website_request_compound_dict = website_request_compound_instance.to_dict()
# create an instance of WebsiteRequestCompound from a dict
website_request_compound_form_dict = website_request_compound.from_dict(website_request_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


