function FilterPriorityAreas(sel_val) {
		    var priorityAreaList = $('id_priority_area');
		    for (var count = priorityAreaList.options.length-1; count >-1; count--){
			    priorityAreaList.options[count] = null;
		    }
		    priorityAreaList.options[0] = new Option('Loading...', '-1', false, false);
		    priorityAreaList.disabled = true;
	    
		    // var makeList = $('id_make');
		    // var make_id = makeList.options[makeList.selectedIndex].value;
		    var country = $('id_country')
		    var country_id = country.options[country.selectedIndex].value;
		    if (country_id > 0){
		    //if (make_id > 0) {
			    new Ajax.Request('/feeds/priority-areas-by-country-id/' + country_id + '/', {
			    //new Ajax.Request('/feeds/models-by-make-id/' + make_id + '/', {
				    method: 'get',
				    onSuccess: function(transport){
					    var response = transport.responseText || 'no response text';
					    var kvpairs = response.split("\n");
					    for (i=0; i<kvpairs.length - 1; i++) {
						    m = kvpairs[i].split(";");
						    var option = new Option(m[1], m[0], false, false);
						    priorityAreaList.options[i] = option;
					    }
					    priorityAreaList.disabled = false;
					    if (sel_val > 0) {
						    priorityAreaList.value = sel_val;
					    }
				    },
				    onFailure: function(){
					    alert('An error occured trying to filter the model list.');					    
					    priorityAreaList.disabled = false;
				    }
			    });
		    }
		    else {
			    priorityAreaList.options[0] = new Option('Select Priority Area', '-1', false, false);
			    priorityAreaList.disabled = true;
		    }
	    }
	    
	    function FilterFacilityCharacters(sel_val) {		    
		    var facList = $('id_facility_character');
		    for (var count = facList.options.length-1; count >-1; count--){
			    facList.options[count] = null;
		    }
		    facList.options[0] = new Option('Loading...', '-1', false, false);
		    facList.disabled = true;
		    FilterTechnologies()
		    // var makeList = $('id_make');
		    // var make_id = makeList.options[makeList.selectedIndex].value;
		    var category = $('id_sector_category')
		    var category_id = category.options[category.selectedIndex].value;
		    if (category_id > 0){
		    //if (make_id > 0) {
			    new Ajax.Request('/feeds/facility-characters-by-sector-category-id/' + category_id + '/', {
			    //new Ajax.Request('/feeds/models-by-make-id/' + make_id + '/', {
				    method: 'get',
				    onSuccess: function(transport){
					    var response = transport.responseText || 'no response text';
					    var kvpairs = response.split("\n");
					    if (kvpairs.length < 2) {
						techList.options[0] = new Option('No Facility Characters', '-1', false, false);
						techList.disabled = true;
						return;
					    }
					    for (i=0; i<kvpairs.length - 1; i++) {
						    m = kvpairs[i].split(";");
						    var option = new Option(m[1], m[0], false, false);
						    facList.options[i] = option;
					    }
					    facList.disabled = false;
					    if (sel_val > 0) {
						    facList.value = sel_val;
					    }
				    },
				    onFailure: function(){
					    alert('An error occured trying to filter the Facility Characteristics list.');					    
					    facList.disabled = true;
				    }
			    });
			FilterTechnologies();    
		    }
		    else {
			    facList.options[0] = new Option('Select Facility Characteristic', '-1', false, false);
			    facList.disabled = true;
		    }
		    FilterTechnologies();
	    }
	    
	    function FilterTechnologies(sel_val) {
		    var techList = $('id_technology');
		    for (var count = techList.options.length-1; count >-1; count--){
			    techList.options[count] = null;
		    }
		    techList.options[0] = new Option('Loading...', '-1', false, false);
		    techList.disabled = true;
	    
		    // var makeList = $('id_make');
		    // var make_id = makeList.options[makeList.selectedIndex].value;
		    var facility = $('id_facility_character')
		    var facility_id = facility.options[facility.selectedIndex].value;
		    if (facility_id > 0){
		    //if (make_id > 0) {
			    new Ajax.Request('/feeds/technologies-by-facility-character-id/' + facility_id + '/', {
			    //new Ajax.Request('/feeds/models-by-make-id/' + make_id + '/', {
				    method: 'get',
				    onSuccess: function(transport){
					    var response = transport.responseText || 'no response text';
					    var kvpairs = response.split("\n");
					    if (kvpairs.length < 2) {
						techList.options[0] = new Option('No Technologies', '-1', false, false);
						techList.disabled = true;
						return;
					    }
					    for (i=0; i<kvpairs.length - 1; i++) {
						    m = kvpairs[i].split(";");
						    var option = new Option(m[1], m[0], false, false);
						    techList.options[i] = option;
					    }
					    techList.disabled = false;
					    if (sel_val > 0) {
						    techList.value = sel_val;
					    }
				    },
				    onFailure: function(){
					    alert('An error occured trying to filter the Technologies list.');					    
					    techList.disabled = true;
				    }
			    });
		    }
		    else {
			    techList.options[0] = new Option('Select Technology', '-1', false, false);
			    techList.disabled = true;
		    }
	    }