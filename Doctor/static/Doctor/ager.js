(function($) {
  function calculateAge(birthday) { // birthday is a date
    var ageDifMs = Date.now() - birthday.getTime();
    var ageDate = new Date(ageDifMs); // miliseconds from epoch
    return Math.abs(ageDate.getUTCFullYear() - 1970);
  }

  $.fn.ager = function(params){

    let defaults = {
      birth: null,
      day_first_suffixes: null,
      day_global_suffix: null,
      text_months: null,
      years_text: "",
      output: "%a %Y (%d/%m/%y)",
      output_type: "text"
    };
    let param = $.extend(defaults, params);

    this.each(function() {
      let birth = param.birth == null ? $(this).text() : param.birth;
      let age = calculateAge(new Date(birth));
      let d = birth.split('-')[2];
      let m = birth.split('-')[1];
      let y = birth.split('-')[0];

      if ((param.day_first_suffixes && param.day_first_suffixes instanceof Array) || param.day_global_suffix != null)
      {
        let day = "";
        if (param.day_first_suffixes[d - 1])
          day = param.day_first_suffixes[d - 1];
        else if (param.day_global_suffix != null)
          day = param.day_global_suffix;
        param.output = param.output.replace(/%s/g, day);
      }
      else
        param.output = param.output.replace(/%s/g, "");
      if (param.text_months && param.text_months instanceof Array && param.text_months[m - 1])
        param.output = param.output.replace(/%N/g, param.text_months[m - 1]);
      param.output = param.output .replace(/%D/g, (d < 10 ? d % 10 : d))
                                  .replace(/%d/g, d)
                                  .replace(/%a/g, age)
                                  .replace(/%y/g, y)
                                  .replace(/%Y/g, param.years_text)
                                  .replace(/%m/g, m)
                                  .replace(/%M/g, (m < 10 ? m % 10 : m));
      if (param.output_type == "html")
        $(this).html(param.output);
      else if (param.output_type == "text")
        $(this).text(param.output);
    });
    return this;
  };
})(jQuery);