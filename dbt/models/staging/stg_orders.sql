select
    o_orderkey  as order_id,
    o_custkey   as customer_id,
    o_totalprice as order_amount,
    o_orderdate as order_date,
    o_orderstatus as order_status
from snowflake_sample_data.tpch_sf1.orders
