select
    c_custkey   as customer_id,
    c_name      as customer_name,
    c_nationkey as nation_id,
    c_mktsegment as market_segment,
    c_acctbal   as account_balance
from snowflake_sample_data.tpch_sf1.customer
