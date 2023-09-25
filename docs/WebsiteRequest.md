# WebsiteRequest

A Website Object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fki_websitetype_id** | **int** | The unique ID of the Websitetype.  Valid values:  |Value|Description| |-|-| |1|Website| |2|Twitter| |3|Facebook| |4|Survey| | 
**s_website_address** | **str** | The URL of the website. | 

## Example

```python
from eZmaxApi.models.website_request import WebsiteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WebsiteRequest from a JSON string
website_request_instance = WebsiteRequest.from_json(json)
# print the JSON string representation of the object
print WebsiteRequest.to_json()

# convert the object into a dict
website_request_dict = website_request_instance.to_dict()
# create an instance of WebsiteRequest from a dict
website_request_form_dict = website_request.from_dict(website_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


