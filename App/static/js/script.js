/**
 * NOTE: All functions are called from forms.py
 */

// 1) Datepicker
$(document).ready(function () {
  $(".datepicker").datepicker({
    yearRange: "-65:-18", // BIRTHDAY (Range: 18 and 65)
    maxDate: "-18Y",
    minDate: "-65Y",
    changeMonth: true,
    changeYear: true,
  });
});

// 2) Enable/Disable 'PROFESSIONAL CARD . [x] I have experience
$(document).ready(function () {
  $(function () {
    Emp();
    $("#emp").click(Emp);
  });
  function Emp() {
    if (this.checked) {
      $("input.emp, textarea.emp").removeAttr("disabled");
    } else {
      $("input.emp, textarea.emp").attr("disabled", true);
    }
  }
});
