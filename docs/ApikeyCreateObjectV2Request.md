# ApikeyCreateObjectV2Request

Request for POST /2/object/apikey

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_apikey** | [**List[ApikeyRequestCompound]**](ApikeyRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.apikey_create_object_v2_request import ApikeyCreateObjectV2Request

# TODO update the JSON string below
json = "{}"
# create an instance of ApikeyCreateObjectV2Request from a JSON string
apikey_create_object_v2_request_instance = ApikeyCreateObjectV2Request.from_json(json)
# print the JSON string representation of the object
print ApikeyCreateObjectV2Request.to_json()

# convert the object into a dict
apikey_create_object_v2_request_dict = apikey_create_object_v2_request_instance.to_dict()
# create an instance of ApikeyCreateObjectV2Request from a dict
apikey_create_object_v2_request_form_dict = apikey_create_object_v2_request.from_dict(apikey_create_object_v2_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


