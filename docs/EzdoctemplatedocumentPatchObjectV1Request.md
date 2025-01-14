# EzdoctemplatedocumentPatchObjectV1Request

Request for PATCH /1/object/ezdoctemplatedocument/{pkiEzdoctemplatedocumentID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezdoctemplatedocument** | [**EzdoctemplatedocumentRequestPatch**](EzdoctemplatedocumentRequestPatch.md) |  | 

## Example

```python
from eZmaxApi.models.ezdoctemplatedocument_patch_object_v1_request import EzdoctemplatedocumentPatchObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzdoctemplatedocumentPatchObjectV1Request from a JSON string
ezdoctemplatedocument_patch_object_v1_request_instance = EzdoctemplatedocumentPatchObjectV1Request.from_json(json)
# print the JSON string representation of the object
print(EzdoctemplatedocumentPatchObjectV1Request.to_json())

# convert the object into a dict
ezdoctemplatedocument_patch_object_v1_request_dict = ezdoctemplatedocument_patch_object_v1_request_instance.to_dict()
# create an instance of EzdoctemplatedocumentPatchObjectV1Request from a dict
ezdoctemplatedocument_patch_object_v1_request_from_dict = EzdoctemplatedocumentPatchObjectV1Request.from_dict(ezdoctemplatedocument_patch_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


