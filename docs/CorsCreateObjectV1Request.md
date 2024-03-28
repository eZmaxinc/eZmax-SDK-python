# CorsCreateObjectV1Request

Request for POST /1/object/cors

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_cors** | [**List[CorsRequestCompound]**](CorsRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.cors_create_object_v1_request import CorsCreateObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of CorsCreateObjectV1Request from a JSON string
cors_create_object_v1_request_instance = CorsCreateObjectV1Request.from_json(json)
# print the JSON string representation of the object
print(CorsCreateObjectV1Request.to_json())

# convert the object into a dict
cors_create_object_v1_request_dict = cors_create_object_v1_request_instance.to_dict()
# create an instance of CorsCreateObjectV1Request from a dict
cors_create_object_v1_request_form_dict = cors_create_object_v1_request.from_dict(cors_create_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


