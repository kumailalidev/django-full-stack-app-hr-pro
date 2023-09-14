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
