```python exec
import reflex as rx
from reflex_image_zoom import image_zoom
from pcweb.pages.pricing.calculator import compute_table_base
```

## Compute Usage

Reflex Cloud is billed on a per second basis so you only pay for when your app is being used by your end users. When your app is idle, you are not charged. 

This allows you to deploy your app on larger sizes and multiple regions without worrying about paying for idle compute. We bill on a per second basis so you only pay for the compute you use.

By default your app stays alive for 5 minutes after the no users are connected. After this time your app will be considered idle and you will not be charged. Start up times usually take less than 1 second for you apps to come back online.

#### Warm vs Cold Start
- Apps below `c2m2` are considered warm starts and are usually less than 1 second.
- If your app is larger than `c2m2` it will be a cold start which takes around 15 seconds. If you want to avoid this you can reserve a machine.

## Compute Pricing Table

```python eval
compute_table_base()
```

## Reserved Machines (Coming Soon)

If you expect your apps to be continuously receiving users, you may want to reserve a machine instead of having us manage your compute. 

This will be a flat monthly rate for the machine.

## Monitoring Usage

To monitor your projects usage, you can go to the billing tab in the Reflex Cloud UI on the project page.

Here you can see the current billing and usage for your project.
