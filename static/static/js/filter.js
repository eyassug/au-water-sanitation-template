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
						facList.options[0] = new Option('No Facility Characters', '-1', false, false);
						facList.disabled = true;
						return;
					    }
                                            facList.options[0] = new Option('Select Facility Character', '-1', true, false);
					    for (i=0; i<kvpairs.length - 1; i++) {
						    m = kvpairs[i].split(";");
						    var option = new Option(m[1], m[0], false, false);
						    facList.options[i+1] = option;
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
                                            techList.options[0] = new Option('Select Technology', '-1', true, false);
					    for (i=0; i<kvpairs.length - 1; i++) {
						    m = kvpairs[i].split(";");
						    var option = new Option(m[1], m[0], false, false);
						    techList.options[i+1] = option;
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
            
            function FilterTechnologiesNew(sel_val,fac_id) {		    
		    var techList = $('id_technology');
		    for (var count = techList.options.length-1; count >-1; count--){
			    techList.options[count] = null;
		    }
		    techList.options[0] = new Option('Loading...', '-1', false, false);
		    techList.disabled = true;
		    // var makeList = $('id_make');
		    // var make_id = makeList.options[makeList.selectedIndex].value;
		    var category = $('id_facility_character')
		    var category_id = category.options[category.selectedIndex].value;
                    if (fac_id) {
                        category_id = fac_id
                    }
                    //alert('Selected Facility Character: ' + category_id);
		    if (category_id > 0){
		    //if (make_id > 0) {
			    new Ajax.Request('/feeds/technologies-by-facility-character-id/' + category_id + '/', {
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
                                            techList.options[0] = new Option('Select Technology', '-1', true, false);
					    for (i=0; i<kvpairs.length - 1; i++) {
						    m = kvpairs[i].split(";");
						    var option = new Option(m[1], m[0], false, false);
						    techList.options[i+1] = option;
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
            
            function FilterTenderProcProperties(sel_val) {		    
		    var propList = $('id_tender_procedure_property');
		    for (var count = propList.options.length-1; count >-1; count--){
			    propList.options[count] = null;
		    }
		    propList.options[0] = new Option('Loading...', '-1', false, false);
		    propList.disabled = true;
		    // var makeList = $('id_make');
		    // var make_id = makeList.options[makeList.selectedIndex].value;
		    var category = $('id_sector_category')
		    var category_id = category.options[category.selectedIndex].value;
		    if (category_id > 0){
		    //if (make_id > 0) {
			    new Ajax.Request('/feeds/tender-proc-properties-by-sector-category-id/' + category_id + '/', {
			    //new Ajax.Request('/feeds/models-by-make-id/' + make_id + '/', {
				    method: 'get',
				    onSuccess: function(transport){
					    var response = transport.responseText || 'no response text';
					    var kvpairs = response.split("\n");
					    if (kvpairs.length < 2) {
						propList.options[0] = new Option('No Tender Proc Properties', '-1', false, false);
						propList.disabled = true;
						return;
					    }
                                            propList.options[0] = new Option('Select Tender Proc Property', '-1', true, false);
					    for (i=0; i<kvpairs.length - 1; i++) {
						    m = kvpairs[i].split(";");
						    var option = new Option(m[1], m[0], false, false);
						    propList.options[i+1] = option;
					    }
					    propList.disabled = false;
					    if (sel_val > 0) {
						    propList.value = sel_val;
					    }
				    },
				    onFailure: function(){
					    alert('An error occured trying to filter the Tender & Proc Properties list.');					    
					    propList.disabled = true;
				    }
			    });   
		    }
		    else {
			    propList.options[0] = new Option('Select Tender & Proc. Property', '-1', false, false);
			    propList.disabled = true;
		    }
	    }
 
 
 (function ( $ ) {
    $.fn.stickyTabs = function() {
        context = this

        // Show the tab corresponding with the hash in the URL, or the first tab.
        var showTabFromHash = function() {
          var hash = window.location.hash;
          var selector = hash ? 'a[href="' + hash + '"]' : 'li.active > a';
          $(selector, context).tab('show');
        }

        // Set the correct tab when the page loads
        showTabFromHash(context)

        // Set the correct tab when a user uses their back/forward button
        window.addEventListener('hashchange', showTabFromHash, false);

        // Change the URL when tabs are clicked
        $('a', context).on('click', function(e) {
          history.pushState(null, null, this.href);
        });

        return this;
    };
}( jQuery ));

 
 
