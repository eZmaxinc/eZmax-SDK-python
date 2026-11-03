# DocumenttypeRequestCompound

A Documenttype Object and children

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_documenttype_id** | **int** | The unique ID of the Documenttype | [optional] 
**obj_documenttype_name** | [**MultilingualDocumenttypeName**](MultilingualDocumenttypeName.md) |  | 
**e_documenttype_step** | [**ComputedEDocumenttypeStep**](ComputedEDocumenttypeStep.md) |  | 
**s_documenttype_defaultfilename** | **str** | The defaultfilename of the Documenttype | 
**b_documenttype_showagent** | **bool** | Whether if it&#39;s an showagent | 
**b_documenttype_isactive** | **bool** | Whether the documenttype is active or not | 
**b_documenttype_isrequired** | **bool** | Whether if it&#39;s an isrequired | 
**b_documenttype_sale** | **bool** | Whether if it&#39;s an sale | 
**b_documenttype_rental** | **bool** | Whether if it&#39;s an rental | 
**b_documenttype_reference** | **bool** | Whether if it&#39;s an reference | 
**b_documenttype_mortgagereference** | **bool** | Whether if it&#39;s an mortgagereference | 
**b_documenttype_evaluation** | **bool** | Whether if it&#39;s an evaluation | 
**b_documenttype_consultation** | **bool** | Whether if it&#39;s an consultation | 
**b_documenttype_otherservices** | **bool** | Whether if it&#39;s an otherservices | 
**b_documenttype_foreclosedsale** | **bool** | Whether if it&#39;s an foreclosedsale | 
**b_documenttype_commercialfunding** | **bool** | Whether if it&#39;s an commercialfunding | 
**b_documenttype_canafe** | **bool** | Whether if it&#39;s an canafe | 
**e_documenttype_ezcom** | [**FieldEDocumenttypeEzcom**](FieldEDocumenttypeEzcom.md) |  | [optional] 
**e_documenttype_privacydefault** | [**FieldEDocumenttypePrivacydefault**](FieldEDocumenttypePrivacydefault.md) |  | 
**e_documenttype_statusdefault** | [**FieldEDocumenttypeStatusdefault**](FieldEDocumenttypeStatusdefault.md) |  | 
**e_documenttype_salebyowner** | [**FieldEDocumenttypeSalebyowner**](FieldEDocumenttypeSalebyowner.md) |  | 
**e_documenttype_saledisplaybyrole** | [**FieldEDocumenttypeSaledisplaybyrole**](FieldEDocumenttypeSaledisplaybyrole.md) |  | 
**e_documenttype_transactiontype** | [**FieldEDocumenttypeTransactiontype**](FieldEDocumenttypeTransactiontype.md) |  | 
**e_documenttype_repossession** | [**FieldEDocumenttypeRepossession**](FieldEDocumenttypeRepossession.md) |  | 
**a_fki_inscriptiontype_id** | **List[int]** |  | 

## Example

```python
from eZmaxApi.models.documenttype_request_compound import DocumenttypeRequestCompound

# TODO update the JSON string below
json = "{}"
# create an instance of DocumenttypeRequestCompound from a JSON string
documenttype_request_compound_instance = DocumenttypeRequestCompound.from_json(json)
# print the JSON string representation of the object
print(DocumenttypeRequestCompound.to_json())

# convert the object into a dict
documenttype_request_compound_dict = documenttype_request_compound_instance.to_dict()
# create an instance of DocumenttypeRequestCompound from a dict
documenttype_request_compound_from_dict = DocumenttypeRequestCompound.from_dict(documenttype_request_compound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


