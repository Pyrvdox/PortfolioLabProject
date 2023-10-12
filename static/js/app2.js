document.addEventListener("DOMContentLoaded", function () {
  const nextStepButton = document.querySelector("button[name='sendform']");

  if (nextStepButton) {
    nextStepButton.addEventListener("click", function () {
      const form = document.querySelector("form[name='form1']");
      if (form) {
        const formData = new FormData(form);
        const formObject = {};
        formData.forEach((value, key) => {
          formObject[key] = value;
        });
        console.log(formObject);

        const spanAll = document.querySelectorAll(".summary--text");
        console.log(spanAll)
        const firstSpan = spanAll[0];
        const secondSpan = spanAll[1];
        firstSpan.textContent = `${formObject.bags} 60L worki zawierające ${formObject.categories}`;
        secondSpan.textContent = `Dla fundacji w mieście ${formObject.city}`;

        const addressElements = document.querySelectorAll(".form-section--column ul li");
        console.log(addressElements)
        addressElements[0].textContent = formObject.address;
        addressElements[1].textContent = formObject.city;
        addressElements[2].textContent = formObject.zip_code;
        addressElements[3].textContent = formObject.phone;
        addressElements[4].textContent = formObject.date;
        addressElements[5].textContent = formObject.time;
        addressElements[6].textContent = formObject.more_info;
        console.log(addressElements[0],addressElements[1],addressElements[2],addressElements[3],addressElements[4],addressElements[5],addressElements[6],)

      }
    });
  }
});


//document.addEventListener("DOMContentLoaded", function () {
//  const sendInfoButton = document.querySelector("button[name='sendallinfo']");});

