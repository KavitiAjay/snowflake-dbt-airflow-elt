select
    c.customer_id,
    c.customer_name,
    c.market_segment,
    count(o.order_id)        as lifetime_orders,
    sum(o.order_amount)      as lifetime_value,
    min(o.order_date)        as first_order_date,
    max(o.order_date)        as latest_order_date
from {{ ref('stg_customers') }} c
left join {{ ref('stg_orders') }} o using (customer_id)
group by 1, 2, 3
