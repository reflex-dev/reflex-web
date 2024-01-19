---
components:
    - rx.radix.primitives.form.FormRoot
    - rx.radix.primitives.form.FormField
    - rx.radix.primitives.form.FormControl
    - rx.radix.primitives.form.FormLabel
    - rx.radix.primitives.form.FormMessage
    - rx.radix.primitives.form.FormSubmit
---

# Form

```python exec
import reflex as rx
import reflex.components.radix.themes as rdxt
import reflex.components.radix.primitives as rdxp
```

Forms are used to collect information from your users. Forms group the inputs and submit them together.

This implementation is based on the [Radix forms](https://www.radix-ui.com/primitives/docs/components/form).

## Basic Example

Here is an example of a form collecting an email address, with built-in validation on the email. If email entered is invalid, the form cannot be submitted. Note that the `form_submit` button is not automatically disabled. It is still clickable, but does not submit the form data. After successful submission, an alert window shows up and the form is cleared. There are a few `flex` containers used in the example to control the layout of the form components.

```python demo
rdxp.form_root(
    rdxp.form_field(
        rdxt.flex(
            rdxp.form_label("Email"),
            rdxp.form_control(
                rdxt.textfield_input(
                    placeholder="Email Address",
                    # type attribute is required for "typeMismatch" validation
                    type="email",
                ),
                as_child=True,
            ),
            rdxp.form_message("Please enter a valid email", match="typeMismatch"),
            rdxp.form_submit(
                  rdxt.button("Submit"),
                  as_child=True,
            ),
            direction="column",
            gap="2",
            align="stretch",
        ),
        name="email",
    ),
    on_submit=lambda _: rx.window_alert("Submitted!"),
    reset_on_submit=True,
)
```

In this example, the `textfield_input` has an attribute `type="email"` and the `form_message` attribute `match="typeMismatch"`. Those are required for the form to validate the input by its type. The prop `as_child="True"` is required when we use other components to construct `form_control` or `form_submit`. In the example, we have used `textfield_input` to construct the `form_control` and `button` the `form_submit`.

## Form Anatomy

```python eval
rx.code_block(
    """form_root(
    form_field(
        form_label(...),
        form_control(...),
        form_message(...),
    ),
    form_submit(...),
)""",
    language="python",
)
```

A `form_root` contains all the parts of a form. The `form_field`, `form_submit`, etc should all be inside a `form_root`. A `form_field` can contain a `form_label`, a `form_control`, and a `form_message`. A `form_label` is a label element. A `form_control` is where the user enters the input or makes selections. By default, `form_control` is a input. You can use your own form components to construct the `form_control` and set the prop `as_child=True`.

```md alert info
The current version of Radix Forms does not support composing `form_control` with other Radix form primitives such as `checkbox`, `select`, etc.
```

The `form_message` is a validation message which is automatically wired (functionality and accessibility). When `form_control` determines the input is invalid, the `form_message` is shown. You set the `match` prop to enable [client side validation](#client-side-validation). You can set the `force_match` prop of `form_message` and `server_invalid` prop of `form_field` together to perform [server side validation](#server-side-validation).

The `form_submit` is by default a button that submits the form. You can use your own button component as a `form_submit` by including that button as a child inside the `form_submit` and set the `as_child` prop to `True`.

The `on_submit` prop of `form_root` accepts an event handler. It is called with the submitted form data dictionary. To clear the form after submission, set the `reset_on_submit=True` prop.

## Data Submission

As previously mentioned, the various pieces of data in the form are submitted together as a dictionary. The form control or the input components must have the `name` attribute. This `name` is the key to get the value from the form data dictionary. If you do not need any validation, you can include the form type components such as Checkbox, Radio Groups, TextArea directly under the `form_root`.

```python demo exec
import reflex as rx
import reflex.components.radix.themes as rdxt
import reflex.components.radix.primitives as rdxp

class RadixFormSubmissionState(rx.State):
    box1: str
    box2: str
    box3: str
    box4: str
    box5: str
    box6: str
    box7: str

    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.box1 = form_data.get("box1")
        self.box2 = form_data.get("box2")
        self.box3 = form_data.get("box3")
        self.box4 = form_data.get("box4")
        self.box5 = form_data.get("box5")
        self.box6 = form_data.get("box6")
        self.box7 = form_data.get("box7")

def radix_form_submission_example():
    return rdxt.flex(
        rdxp.form_root(
            rdxt.flex(
                rdxt.flex(
                    rdxt.checkbox(
                        default_checked=True,
                        name="box1",
                    ),
                    rdxt.text("box1 checkbox"),
                    direction="row",
                    gap="2",
                    align="center",
                ),
                rdxt.radio_group_root(
                    rdxt.flex(
                        rdxt.radio_group_item(value="1"),
                        "1",
                        direction="row",
                        align="center",
                        gap="2",
                    ),
                    rdxt.flex(
                        rdxt.radio_group_item(value="2"),
                        "2",
                        direction="row",
                        align="center",
                        gap="2",
                    ),
                    rdxt.flex(
                        rdxt.radio_group_item(value="3"),
                        "3",
                        direction="row",
                        align="center",
                        gap="2",
                    ),
                    default_value="1",
                    name="box2",
                ),
                rdxt.textfield_input(
                    placeholder="box3 textfield input",
                    name="box3",
                ),
                rdxt.select_root(
                    rdxt.select_trigger(
                        placeholder="box4 select",
                    ),
                    rdxt.select_content(
                        rdxt.select_group(
                            rdxt.select_item(
                                "Orange",
                                value="orange"
                            ),
                            rdxt.select_item(
                                "Apple",
                                value="apple"
                            ),
                        ),
                    ),
                    name="box4",
                ),
                rdxt.flex(
                    rdxt.switch(
                        default_checked=True,
                        name="box5",
                    ),
                    "box5 switch",
                    gap="2",
                    align="center",
                    direction="row",
                ),
                rdxt.flex(
                    rdxt.slider(
                        default_value=[40],
                        width="100%",
                        name="box6",
                    ),
                    "box6 slider",
                    direction="row",
                    gap="2",
                    align="center",
                ),
                rdxt.textarea(
                    placeholder="Enter for box7 textarea",
                    name="box7",
                ),
                rdxp.form_submit(
                    rdxt.button("Submit"),
                    as_child=True,
                ),
                direction="column",
                gap="4",
            ),
            on_submit=RadixFormSubmissionState.handle_submit,
        ),
        rdxt.separator(size="4"),
        rdxt.text(
            "Results",
            weight="bold",
        ),
        rdxt.text(
            "box1: ",
            RadixFormSubmissionState.box1,
        ),
        rdxt.text(
            "box2: ",
            RadixFormSubmissionState.box2,
        ),
        rdxt.text(
            "box3: ",
            RadixFormSubmissionState.box3,
        ),
        rdxt.text(
            "box4: ",
            RadixFormSubmissionState.box4,
        ),
        rdxt.text(
            "box5: ",
            RadixFormSubmissionState.box5,
        ),
        rdxt.text(
            "box6: ",
            RadixFormSubmissionState.box6,
        ),
        rdxt.text(
            "box7: ",
            RadixFormSubmissionState.box7,
        ),
        direction="column",
        gap="4",
    )
```

## Validation

### Client Side Validation

Client side validation is achieved by examining the property of an interface of HTML elements called `ValidityState`. By setting the `match` prop of `form_message`, you can determine when the message should be displayed. The `match` prop takes the following values: `"badInput" | "patternMismatch" | "rangeOverflow" | "rangeUnderflow" | "stepMismatch" | "tooLong" | "tooShort" | "typeMismatch" | "valueMissing"`. For example, `"typeMismatch"` is set to `True` when an input element has a `type` attribute and the entered value is not valid for the `type`. If the input is specified as `type="url"`, it is expected to start with `http://` or `https://`. For the list of supported types, please refer to [HTML input element docs](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#type). The above references are all part of the HTML standards. For more details, please refer to [ValidityState docs](https://developer.mozilla.org/en-US/docs/Web/API/ValidityState) and further more the reference links on that page.

Below is an example of a form that collects a `number` from a `textfield_input`. We require a range of `[30, 100]` (both ends of the range are inclusive: `30` and `100` are valid). When you enter a number smaller than `30`, a message below the input field is printed: `"Please enter a number >= 30"`. This is because we have set `min=30` on the `textfield_input` and `match="rangeUnderflow"` on the `form_message`. Similarly, when you enter a number larger than `100`, this message `"Please enter a number <= 100"` is displayed. You can see the `max=100` attribute on the `textfield_input` and `match="rangeOverflow"` on `form_message`.

```python demo
rdxp.form_root(
    rdxp.form_field(
        rdxt.flex(
            rdxp.form_label("Requires number in range [30, 100]"),
            rdxp.form_control(
                rdxt.textfield_input(
                    placeholder="Enter a number",
                    type="number",
                    max=100,
                    min=30
                ),
                as_child=True,
            ),
            rdxp.form_message("Please enter a number <= 100", match="rangeOverflow"),
            rdxp.form_message("Please enter a number >= 30", match="rangeUnderflow"),
            rdxp.form_submit(
                rdxt.button("Submit"),
                as_child=True,
            ),
            direction="column",
            gap="2",
            align="stretch",
        ),
        name="some_number",
    ),
    on_submit=lambda _: rx.window_alert("Submitted!"),
    reset_on_submit=True,
)
```

Here is an example if you want the input text to be at least a certain length. You notice the attribute `min_length` is written as snake case. Behind the scene, we automatically convert this to the camel case `minLength` used in the frontend.

```python demo
rdxp.form_root(
    rdxp.form_field(
        rdxt.flex(
            rdxp.form_label("Please choose a password of length >= 8 characters"),
            rdxp.form_control(
                rdxt.textfield_input(
                    placeholder="Enter your password",
                    min_length=8
                ),
                as_child=True,
            ),
            rdxp.form_message("Please enter a password length >= 8", match="tooShort"),
            rdxp.form_submit(
                rdxt.button("Submit"),
                as_child=True,
            ),
            direction="column",
            gap="2",
            align="stretch",
        ),
        name="user_password",
    ),
    on_submit=lambda _: rx.window_alert("Submitted!"),
    reset_on_submit=True,
)
```

If the input follows certain patterns, setting `pattern` on the input and `match="patternMismatch"` on the `form_message` could be useful. Below is an example of a form that requires input to be precisely 10 digits. You can find more information at [ValidityState: patternMismatch property](https://developer.mozilla.org/en-US/docs/Web/API/ValidityState/patternMismatch).

```python demo
rdxp.form_root(
    rdxp.form_field(
        rdxt.flex(
            rdxp.form_label("Please enter your phone number with only digits. Let's say in your region the phone number is exactly 10 digits long."),
            rdxp.form_control(
                rdxt.textfield_input(
                    placeholder="Enter your your phone number",
                    type="text",
                    pattern="[0-9]{10}",
                ),
                as_child=True,
            ),
            rdxp.form_message(
                "Please enter a valid phone number",
                match="patternMismatch",
            ),
            rdxp.form_submit(
                rdxt.button("Submit"),
                as_child=True,
            ),
            direction="column",
            gap="2",
            align="stretch",
        ),
        name="phone_number",
    ),
    on_submit=lambda _: rx.window_alert("Submitted!"),
    reset_on_submit=True,
)
```

Below is an example of `"typeMismatch"` validation.

```python demo
rdxp.form_root(
    rdxp.form_field(
        rdxt.flex(
            rdxp.form_label("Please enter a valid URL starting with http or https"),
            rdxp.form_control(
                rdxt.textfield_input(
                    placeholder="Enter your URL",
                    type="url",
                ),
                as_child=True,
            ),
            rdxp.form_message("Please enter a valid URL", match="typeMismatch"),
            rdxp.form_submit(
                rdxt.button("Submit"),
                as_child=True,
            ),
            direction="column",
            gap="2",
            align="stretch",
        ),
        name="user_url",
    ),
    on_submit=lambda _: rx.window_alert("Submitted!"),
    reset_on_submit=True,
)
```

### Server Side Validation

Server side validation is done through `Computed Vars` on the State. The `Var` returns a boolean flag indicating when input is invalid. You pass the `Var` to both the `server_invalid` prop on `form_field` and the `force_match` prop on `form_message`. There is an example how to do that in the [Final Example](#final-example).

## Final Example

In the final example, we show a form that collects username and email during sign-up and validates them using server side validation. When server side validation fails, messages are displayed in red to show what is not accepted in the form, and the submit button is disabled. After submission, the collected form data is displayed in texts below the form and the form is cleared.

```python demo exec
import re
import reflex as rx
import reflex.components.radix.themes as rdxt
import reflex.components.radix.primitives as rdxp

class RadixFormState(rx.State):
    # These track the user input real time for validation
    user_entered_username: str
    user_entered_email: str

    # These are the submitted data
    username: str
    email: str

    mock_username_db: list[str] = ["reflex", "admin"]

    @rx.var
    def invalid_email(self) -> bool:
        return not re.match(r"[^@]+@[^@]+\.[^@]+", self.user_entered_email)

    @rx.var
    def username_empty(self) -> bool:
        return not self.user_entered_username.strip()

    @rx.var
    def username_is_taken(self) -> bool:
        return self.user_entered_username in self.mock_username_db

    @rx.var
    def input_invalid(self) -> bool:
        return self.invalid_email or self.username_is_taken or self.username_empty

    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.username = form_data.get("username")
        self.email = form_data.get("email")

def radix_form_example():
    return rdxt.flex(
        rdxp.form_root(
            rdxt.flex(
                rdxp.form_field(
                    rdxt.flex(
                        rdxp.form_label("Username"),
                        rdxp.form_control(
                            rdxt.textfield_input(
                                placeholder="Username",
                                on_change=RadixFormState.set_user_entered_username,
                            ),
                            as_child=True,
                        ),
                        # server side validation message can be displayed inside a rx.cond
                        rx.cond(
                            RadixFormState.username_empty,
                            rdxp.form_message(
                                "Username cannot be empty",
                                color="var(--red-11)",
                            ),
                        ),
                        # server side validation message can be displayed by `force_match` prop
                        rdxp.form_message(
                            "Username already taken",
                            # this is a workaround:
                            # `force_match` does not work without `match`
                            # In this case, we do not want client side validation
                            # and intentionally not set `required` on the input
                            # so "valueMissing" is always false
                            match="valueMissing",
                            force_match=RadixFormState.username_is_taken,
                            color="var(--red-11)",
                        ),
                        direction="column",
                        gap="2",
                        align="stretch",
                    ),
                    name="username",
                    server_invalid=RadixFormState.username_is_taken,
                ),
                rdxp.form_field(
                    rdxt.flex(
                        rdxp.form_label("Email"),
                        rdxp.form_control(
                            rdxt.textfield_input(
                                placeholder="Email Address",
                                on_change=RadixFormState.set_user_entered_email,
                            ),
                            as_child=True,
                        ),
                        rdxp.form_message(
                            "A valid Email is required",
                            match="valueMissing",
                            force_match=RadixFormState.invalid_email,
                            color="var(--red-11)",
                        ),
                        direction="column",
                        gap="2",
                        align="stretch",
                    ),
                    name="email",
                    server_invalid=RadixFormState.invalid_email,
                ),
                rdxp.form_submit(
                    rdxt.button(
                        "Submit",
                        disabled=RadixFormState.input_invalid,
                    ),
                    as_child=True,
                ),
                direction="column",
                gap="4",
                width="25em",
            ),
            on_submit=RadixFormState.handle_submit,
            reset_on_submit=True,
        ),
        rdxt.separator(size="4"),
        rdxt.text(
            "Username submitted: ",
            rdxt.text(
                RadixFormState.username,
                weight="bold",
                color="var(--accent-11)",
            ),
        ),
        rdxt.text(
            "Email submitted: ",
            rdxt.text(
                RadixFormState.email,
                weight="bold",
                color="var(--accent-11)",
            ),
        ),
        direction="column",
        gap="4",
    )
```
