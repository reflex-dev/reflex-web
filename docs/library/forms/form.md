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
    on_submit=lambda form_data: rx.window_alert(form_data.to_string()),
    reset_on_submit=True,
)
```

In this example, the `textfield_input` has an attribute `type="email"` and the `form_message` has the attribute `match="typeMismatch"`. Those are required for the form to validate the input by its type. The prop `as_child="True"` is required when using other components to construct a Form component. This example has used `textfield_input` to construct the Form Control and `button` the Form Submit.

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

A Form Root (`form_root`) contains all the parts of a form. The Form Field (`form_field`), Form Submit (`form_submit`), etc should all be inside a Form Root. A Form Field can contain a Form Label (`form_label`), a Form Control (`form_control`), and a Form Message (`form_message`). A Form Label is a label element. A Form Control is where the user enters the input or makes selections. By default, the Form Control is a input. Using other form components to construct the Form Control is supported. To do that, set the prop `as_child=True` on the Form Control.

```md alert info
The current version of Radix Forms does not support composing **Form Control** with other Radix form primitives such as **Checkbox**, **Select**, etc.
```

The Form Message is a validation message which is automatically wired (functionality and accessibility). When the Form Control determines the input is invalid, the Form Message is shown. The `match` prop is to enable [client side validation](#client-side-validation). To perform [server side validation](#server-side-validation), **both** the `force_match` prop of the Form Control and the `server_invalid` prop of the Form Field are set together.

The Form Submit is by default a button that submits the form. To use another button component as a Form Submit, include that button as a child inside `form_submit` and set the prop `as_child=True`.

The `on_submit` prop of the Form Root accepts an event handler. It is called with the submitted form data dictionary. To clear the form after submission, set the `reset_on_submit=True` prop.

## Data Submission

As previously mentioned, the various pieces of data in the form are submitted together as a dictionary. The form control or the input components must have the `name` attribute. This `name` is the key to get the value from the form data dictionary. If no validation is needed, the form type components such as Checkbox, Radio Groups, TextArea can be included directly under the Form Root instead of inside a Form Control.

```python demo exec
import reflex as rx
import reflex.components.radix.themes as rdxt
import reflex.components.radix.primitives as rdxp

class RadixFormSubmissionState(rx.State):
    form_data: dict

    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        self.form_data = form_data

    @rx.var
    def form_data_keys(self) -> list:
        return list(self.form_data.keys())

    @rx.var
    def form_data_values(self) -> list:
        return list(self.form_data.values())


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
        rx.foreach(RadixFormSubmissionState.form_data_keys,
            lambda key, idx: rdxt.text(key, " : ", RadixFormSubmissionState.form_data_values[idx])
        ),
        direction="column",
        gap="4",
    )
```

## Validation

### Client Side Validation

Client side validation is achieved by examining the property of an interface of HTML elements called **ValidityState**. The `match` prop of the Form Message determines when the message should be displayed. The valid `match` prop values can be found in the **props** tab at the top of this page. For example, `"typeMismatch"` is set to `True` when an input element has a `type` attribute and the entered value is not valid for the `type`. If the input is specified as `type="url"`, it is expected to start with `http://` or `https://`. For the list of supported types, please refer to [HTML input element docs](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input#type). The above references are all part of the HTML standards. For more details, please refer to [ValidityState docs](https://developer.mozilla.org/en-US/docs/Web/API/ValidityState) and further more the reference links on that page.

Below is an example of a form that collects a **number** from a `textfield_input`. The number is in the range of **[30, 100]** (both ends of the range are inclusive: **30** and **100** are valid). When a number smaller than **30** is entered, a message below the input field is printed: **Please enter a number >= 30**. This is because `min=30` is set on the `textfield_input` and `match="rangeUnderflow"` on the `form_message`. Similarly, when a number larger than **100** is entered, this message **Please enter a number <= 100** is displayed. Note the `max=100` attribute on the `textfield_input` and `match="rangeOverflow"` on the `form_message`.

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
    on_submit=lambda form_data: rx.window_alert(form_data.to_string()),
    reset_on_submit=True,
)
```

Here is an example where the input text is expected to be at least a certain length. Note that the attribute `min_length` is written as snake case. Behind the scene, Reflex automatically convert this to the camel case `minLength` used in the frontend.

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
    on_submit=lambda form_data: rx.window_alert(form_data.to_string()),
    reset_on_submit=True,
)
```

If the input follows certain patterns, setting `pattern` on the input and `match="patternMismatch"` on the `form_message` could be useful. Below is an example of a form that requires input to be precisely 10 digits. More information is available at [ValidityState: patternMismatch property](https://developer.mozilla.org/en-US/docs/Web/API/ValidityState/patternMismatch).

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
    on_submit=lambda form_data: rx.window_alert(form_data.to_string()),
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
    on_submit=lambda form_data: rx.window_alert(form_data.to_string()),
    reset_on_submit=True,
)
```

### Server Side Validation

Server side validation is done through **Computed Vars** on the State. The **Var** should return a boolean flag indicating when input is invalid. Set that **Var** on both the `server_invalid` prop of `form_field` and the `force_match` prop of `form_message`. There is an example how to do that in the [Final Example](#final-example).

## Final Example

The final example shows a form that collects username and email during sign-up and validates them using server side validation. When server side validation fails, messages are displayed in red to show what is not accepted in the form, and the submit button is disabled. After submission, the collected form data is displayed in texts below the form and the form is cleared.

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
                                # workaround: `name` seems to be required when on_change is set
                                on_change=RadixFormState.set_user_entered_username,
                                name="username",
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
                            # This case does not want client side validation
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
                                name="email",
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
