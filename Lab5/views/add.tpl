% rebase('layout.tpl', title="New Blog")


<div class="jumbotron">
    <h1>Add Blog</h1>
</div>

<form name="frmAddBlog" action="/add_blog" method="post">
	<table class="table">
		<tr>
			<td class="col-md-2">Blog Title</td>
			<td class="col-md-2"><input type="text" name="txtTitle" class="form-control"></td>
		</tr>

		<tr>
			<td class="col-md-2">Content</td>
			<td class="col-md-2"><textarea name="txtContent" class="form-control"></textarea></td>
		</tr>

		<tr>
			<td class="col-md-2">Tags</td>
			<td><input type="text" id="txtTag"> <button type="button" id="btnTag" onclick="addTags()"  class="btn btn-primary">Tag</button> </td>
			<td class="col-md-2">
			<select id="ddlTags" multiple>

			</select>
			<button type="button" id="btnTag" onclick="removeTags()"  class="btn btn-primary">UnTag</button> 
			</td>


			<div id="tagsDiv">
			</div>

		</tr>
		<tr>
			<td class="col-md-2"></td></a>
			<td class="col-md-2">
				<input class="btn btn-primary" type="submit" value="Submit">
				<a class="btn btn-primary" href="/" role="button">Cancel</a>
			</td>
		</tr>
	</table>
</form>

<script type="text/javascript">

function addTags(){
var tags = document.getElementById("ddlTags");

var tag = document.getElementById("txtTag");

var option = document.createElement("option");
option.text = tag.value;
option.value = tag.value;
tags.add(option);

var div = document.getElementById("tagsDiv");
var hidTag = document.createElement("input");
hidTag.type="hidden";
hidTag.name="txtTags";
hidTag.value = tag.value;
hidTag.id = tag.value;
div.appendChild(hidTag);

tag.value = "";

}

function removeTags(){
var tags = document.getElementById("ddlTags");
var tagToRemove = document.getElementById(tags.options[tags.selectedIndex].value);
var div = document.getElementById("tagsDiv");
div.removeChild(tagToRemove);
tags.remove(tags.selectedIndex);
}
</script>