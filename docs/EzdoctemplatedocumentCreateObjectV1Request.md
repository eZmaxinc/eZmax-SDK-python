# EzdoctemplatedocumentCreateObjectV1Request

Request for POST /1/object/ezdoctemplatedocument

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezdoctemplatedocument** | [**List[EzdoctemplatedocumentRequestCompound]**](EzdoctemplatedocumentRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezdoctemplatedocument_create_object_v1_request import EzdoctemplatedocumentCreateObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzdoctemplatedocumentCreateObjectV1Request from a JSON string
ezdoctemplatedocument_create_object_v1_request_instance = EzdoctemplatedocumentCreateObjectV1Request.from_json(json)
# print the JSON string representation of the object
print(EzdoctemplatedocumentCreateObjectV1Request.to_json())

# convert the object into a dict
ezdoctemplatedocument_create_object_v1_request_dict = ezdoctemplatedocument_create_object_v1_request_instance.to_dict()
# create an instance of EzdoctemplatedocumentCreateObjectV1Request from a dict
ezdoctemplatedocument_create_object_v1_request_from_dict = EzdoctemplatedocumentCreateObjectV1Request.from_dict(ezdoctemplatedocument_create_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


