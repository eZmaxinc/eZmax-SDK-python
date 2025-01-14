# WebsiteResponseCompound

A Website Object and children to create a complete structure

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_website_id** | **int** | The unique ID of the Website Default | 
**fki_websitetype_id** | **int** | The unique ID of the Websitetype.  Valid values:  |Value|Description| |-|-| |1|Website| |2|Twitter| |3|Facebook| |4|Survey| | 
**s_website_address** | **str** | The URL of the website. | 

## Example

```python
from eZmaxApi.models.website_response_compound import WebsiteResponseCompound

# TODO update the JSON string below
json = "{}"
# create an instance of WebsiteResponseCompound from a JSON string
website_response_compound_instance = WebsiteResponseCompound.from_json(json)
# print the JSON string representation of the object
print(WebsiteResponseCompound.to_json())

# convert the object into a dict
website_response_compound_dict = website_response_compound_instance.to_dict()
# create an instance of WebsiteResponseCompound from a dict
website_response_compound_from_dict = WebsiteResponseCompound.from_dict(website_response_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


