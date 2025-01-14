# EzdoctemplatedocumentEditObjectV1Request

Request for PUT /1/object/ezdoctemplatedocument/{pkiEzdoctemplatedocumentID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezdoctemplatedocument** | [**EzdoctemplatedocumentRequestCompound**](EzdoctemplatedocumentRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezdoctemplatedocument_edit_object_v1_request import EzdoctemplatedocumentEditObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzdoctemplatedocumentEditObjectV1Request from a JSON string
ezdoctemplatedocument_edit_object_v1_request_instance = EzdoctemplatedocumentEditObjectV1Request.from_json(json)
# print the JSON string representation of the object
print(EzdoctemplatedocumentEditObjectV1Request.to_json())

# convert the object into a dict
ezdoctemplatedocument_edit_object_v1_request_dict = ezdoctemplatedocument_edit_object_v1_request_instance.to_dict()
# create an instance of EzdoctemplatedocumentEditObjectV1Request from a dict
ezdoctemplatedocument_edit_object_v1_request_from_dict = EzdoctemplatedocumentEditObjectV1Request.from_dict(ezdoctemplatedocument_edit_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


