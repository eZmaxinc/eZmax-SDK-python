# SystemconfigurationEditObjectV2Request

Request for PUT /2/object/systemconfiguration/{pkiSystemconfigurationID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_systemconfiguration** | [**SystemconfigurationRequestCompoundV2**](SystemconfigurationRequestCompoundV2.md) |  | 

## Example

```python
from eZmaxApi.models.systemconfiguration_edit_object_v2_request import SystemconfigurationEditObjectV2Request

# TODO update the JSON string below
json = "{}"
# create an instance of SystemconfigurationEditObjectV2Request from a JSON string
systemconfiguration_edit_object_v2_request_instance = SystemconfigurationEditObjectV2Request.from_json(json)
# print the JSON string representation of the object
print(SystemconfigurationEditObjectV2Request.to_json())

# convert the object into a dict
systemconfiguration_edit_object_v2_request_dict = systemconfiguration_edit_object_v2_request_instance.to_dict()
# create an instance of SystemconfigurationEditObjectV2Request from a dict
systemconfiguration_edit_object_v2_request_from_dict = SystemconfigurationEditObjectV2Request.from_dict(systemconfiguration_edit_object_v2_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


