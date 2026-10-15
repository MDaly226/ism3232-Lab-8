from business_rules import (
    apply_discount,
    calculate_total,
    get_approval_tier,
    requires_review,
)

# add sample inputs
price, qty = 450.00, 3

total = calculate_total(price, qty)
review = requires_review(total)
tier = get_approval_tier(total)
discounted_price = apply_discount(price)

print(f"Total: {total:.2f}")
print(f"Requires Review: {review:.2f}")
print(f"Approval Tier: {tier:.2f}")
print(f"10% discount: {discounted_price:.2f}")
