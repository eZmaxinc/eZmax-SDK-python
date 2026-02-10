# EzsigntemplateannotationCreateObjectV1Request

Request for POST /1/object/ezsigntemplateannotation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsigntemplateannotation** | [**List[EzsigntemplateannotationRequestCompound]**](EzsigntemplateannotationRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplateannotation_create_object_v1_request import EzsigntemplateannotationCreateObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplateannotationCreateObjectV1Request from a JSON string
ezsigntemplateannotation_create_object_v1_request_instance = EzsigntemplateannotationCreateObjectV1Request.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplateannotationCreateObjectV1Request.to_json())

# convert the object into a dict
ezsigntemplateannotation_create_object_v1_request_dict = ezsigntemplateannotation_create_object_v1_request_instance.to_dict()
# create an instance of EzsigntemplateannotationCreateObjectV1Request from a dict
ezsigntemplateannotation_create_object_v1_request_from_dict = EzsigntemplateannotationCreateObjectV1Request.from_dict(ezsigntemplateannotation_create_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


