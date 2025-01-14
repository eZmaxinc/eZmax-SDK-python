# WebsiteResponse

A Website Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_website_id** | **int** | The unique ID of the Website Default | 
**fki_websitetype_id** | **int** | The unique ID of the Websitetype.  Valid values:  |Value|Description| |-|-| |1|Website| |2|Twitter| |3|Facebook| |4|Survey| | 
**s_website_address** | **str** | The URL of the website. | 

## Example

```python
from eZmaxApi.models.website_response import WebsiteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WebsiteResponse from a JSON string
website_response_instance = WebsiteResponse.from_json(json)
# print the JSON string representation of the object
print(WebsiteResponse.to_json())

# convert the object into a dict
website_response_dict = website_response_instance.to_dict()
# create an instance of WebsiteResponse from a dict
website_response_from_dict = WebsiteResponse.from_dict(website_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


