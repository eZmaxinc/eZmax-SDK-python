# CorsEditObjectV1Request

Request for PUT /1/object/cors/{pkiCorsID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_cors** | [**CorsRequestCompound**](CorsRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.cors_edit_object_v1_request import CorsEditObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of CorsEditObjectV1Request from a JSON string
cors_edit_object_v1_request_instance = CorsEditObjectV1Request.from_json(json)
# print the JSON string representation of the object
print CorsEditObjectV1Request.to_json()

# convert the object into a dict
cors_edit_object_v1_request_dict = cors_edit_object_v1_request_instance.to_dict()
# create an instance of CorsEditObjectV1Request from a dict
cors_edit_object_v1_request_form_dict = cors_edit_object_v1_request.from_dict(cors_edit_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


