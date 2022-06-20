# EzsigntemplatesignaturecustomdateRequest

An Ezsigntemplatesignaturecustomdate Object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**i_ezsigntemplatesignaturecustomdate_x** | [**FieldIEzsigntemplatesignaturecustomdateX**](FieldIEzsigntemplatesignaturecustomdateX.md) |  | 
**i_ezsigntemplatesignaturecustomdate_y** | [**FieldIEzsigntemplatesignaturecustomdateY**](FieldIEzsigntemplatesignaturecustomdateY.md) |  | 
**s_ezsigntemplatesignaturecustomdate_format** | **str** | The custom date format to use  You can use the codes below and they will be replaced at signature time. Text values like month and day names will be rendered in the proper language. Other text will be left as-is.  The codes examples below are based on the following datetime: Thursday, January 6, 2022 at 08:07:09 EST  For example, the format \&quot;Signature date: {MM}/{DD}/{YYYY} {hh}:{mm}\&quot; would become \&quot;Signature date: 01/06/2022 08:07\&quot;  **Year**  | Code | Example | | - | - | | {YYYY} | 2022 | | {YY} | 22 |  **Month**  | Code | Example | | - | - | | {MonthCapitalize} | Janvier | | {Month} | janvier | | {MM} | 01 | | {M} | 1 |  **Day**  | Code | Example | | - | - | | {DayCapitalize} | Jeudi | | {Day} | jeudi | | {DD} | 06 | | {D} | 6 |  **Hour**  | Code | Example | | - | - | | {hh} | 08 |  **Minute**  | Code | Example | | - | - | | {mm} | 07 |  **Second**  | Code | Example | | - | - | | {ss} | 09 |        **Timezone**  | Code | Example | | - | - | | {Z} | EST |       **Time**  | Code | Example | | - | - | | {Time} | 08:07:09 |   | {TimeZ} | 08:07:09 EST |     **Date**  | Code | Example | | - | - | | {Date} | 2022-01-06 |   | {DateText} | 1er Janvier 2022 |  **Full**  | Code | Example | | - | - | | {DateTime} | 2022-01-06 08:07:09 |   | {DateTimeZ} | 2022-01-06 08:07:09 EST |  | 
**pki_ezsigntemplatesignaturecustomdate_id** | [**FieldPkiEzsigntemplatesignaturecustomdateID**](FieldPkiEzsigntemplatesignaturecustomdateID.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


