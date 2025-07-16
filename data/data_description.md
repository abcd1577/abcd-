# 数据说明

本项目使用 Datawhale AI 夏令营提供的“新增用户预测”基线数据集，来自 ModelScope 平台。

## 数据集

- **train.csv**：训练数据集，包含用户特征和目标变量（约283MB）。
- **testA_data.csv**：测试数据集，用于生成预测结果（约92MB）。

## 获取数据

- 数据来源：ModelScope 平台
- 下载链接：[Datawhale/AISumerCamp_new_user_forecast_baseline](https://www.modelscope.cn/datasets/Datawhale/AISumerCamp_new_user_forecast_baseline)
- 访问 ModelScope 网站，点击“下载”按钮即可获取数据集（无需注册）。

## 数据格式

- **train.csv**：字段包括：
  - `mid`：用户行为模块ID
  - `eid`：用户行为事件ID
  - `did`：用户ID
  - `device_brand`：设备品牌/厂商
  - `ntt`：网络类型
  - `operator`：运营商
  - `common_country`：国家
  - `common_province`：省份
  - `common_city`：城市
  - `appver`：应用版本
  - `channel`：应用渠道
  - `common_ts`：事件发生时间（毫秒时间戳）
  - `os_type`：操作系统（Android 或 iOS）
  - `udmap`：事件自定义属性（JSON 格式，含 botId 和 pluginId）
  - `is_new_did`：预测目标（是否为新增用户，0 或 1）
- **testA_data.csv**：字段与 train.csv 相同，但无 `is_new_did` 列。

## 注意事项

- `udmap` 需解析 JSON 提取 `botId` 和 `pluginId`。
- `common_ts` 为毫秒时间戳，可转换为日期时间特征。
