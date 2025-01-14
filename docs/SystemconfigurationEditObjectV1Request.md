# SystemconfigurationEditObjectV1Request

Request for PUT /1/object/systemconfiguration/{pkiSystemconfigurationID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_systemconfiguration** | [**SystemconfigurationRequestCompound**](SystemconfigurationRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.systemconfiguration_edit_object_v1_request import SystemconfigurationEditObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of SystemconfigurationEditObjectV1Request from a JSON string
systemconfiguration_edit_object_v1_request_instance = SystemconfigurationEditObjectV1Request.from_json(json)
# print the JSON string representation of the object
print(SystemconfigurationEditObjectV1Request.to_json())

# convert the object into a dict
systemconfiguration_edit_object_v1_request_dict = systemconfiguration_edit_object_v1_request_instance.to_dict()
# create an instance of SystemconfigurationEditObjectV1Request from a dict
systemconfiguration_edit_object_v1_request_from_dict = SystemconfigurationEditObjectV1Request.from_dict(systemconfiguration_edit_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


