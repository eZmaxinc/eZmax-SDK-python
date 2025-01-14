# EzsigntemplatedocumentCreateObjectV1Request

Request for POST /1/object/ezsigntemplatedocument

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsigntemplatedocument** | [**List[EzsigntemplatedocumentRequestCompound]**](EzsigntemplatedocumentRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatedocument_create_object_v1_request import EzsigntemplatedocumentCreateObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatedocumentCreateObjectV1Request from a JSON string
ezsigntemplatedocument_create_object_v1_request_instance = EzsigntemplatedocumentCreateObjectV1Request.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatedocumentCreateObjectV1Request.to_json())

# convert the object into a dict
ezsigntemplatedocument_create_object_v1_request_dict = ezsigntemplatedocument_create_object_v1_request_instance.to_dict()
# create an instance of EzsigntemplatedocumentCreateObjectV1Request from a dict
ezsigntemplatedocument_create_object_v1_request_from_dict = EzsigntemplatedocumentCreateObjectV1Request.from_dict(ezsigntemplatedocument_create_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


