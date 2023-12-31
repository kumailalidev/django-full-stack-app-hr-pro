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

// 3) Enable/Disable 'FINISHED DATE (Card professional)'.
// [x] I am employed = Disabled
$(function () {
  Exp();
  $("#exp").click(Exp);
});
function Exp() {
  if (this.checked) {
    $("input#go").attr("disabled", true);
    $("#go").val(""); // clear to prevent sending data.
  } else {
    $("input#go").removeAttr("disabled");
  }
}

// 4) Enable/Disable 'Finished date (Card Educational)'.
// If status course is 'Completed', enable the finished input date
// Pure JS
function statusCourse(edu) {
  var x = document.getElementsByName("finished_course");
  for (var j = 0; j < x.length; j++) {
    x[j].disabled = !(edu.value == "Completed");
    x[j].value = "";
  }
}
