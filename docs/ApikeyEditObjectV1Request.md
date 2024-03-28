# ApikeyEditObjectV1Request

Request for PUT /1/object/apikey/{pkiApikeyID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_apikey** | [**ApikeyRequestCompound**](ApikeyRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.apikey_edit_object_v1_request import ApikeyEditObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of ApikeyEditObjectV1Request from a JSON string
apikey_edit_object_v1_request_instance = ApikeyEditObjectV1Request.from_json(json)
# print the JSON string representation of the object
print(ApikeyEditObjectV1Request.to_json())

# convert the object into a dict
apikey_edit_object_v1_request_dict = apikey_edit_object_v1_request_instance.to_dict()
# create an instance of ApikeyEditObjectV1Request from a dict
apikey_edit_object_v1_request_form_dict = apikey_edit_object_v1_request.from_dict(apikey_edit_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


