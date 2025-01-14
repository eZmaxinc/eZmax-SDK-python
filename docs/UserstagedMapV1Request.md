# UserstagedMapV1Request

Request for POST /1/object/userstaged/{pkiUserstagedID}/map

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fki_user_id** | **int** | The unique ID of the User | 

## Example

```python
from eZmaxApi.models.userstaged_map_v1_request import UserstagedMapV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of UserstagedMapV1Request from a JSON string
userstaged_map_v1_request_instance = UserstagedMapV1Request.from_json(json)
# print the JSON string representation of the object
print(UserstagedMapV1Request.to_json())

# convert the object into a dict
userstaged_map_v1_request_dict = userstaged_map_v1_request_instance.to_dict()
# create an instance of UserstagedMapV1Request from a dict
userstaged_map_v1_request_from_dict = UserstagedMapV1Request.from_dict(userstaged_map_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


