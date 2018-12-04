% rebase('layout.tpl', title="Search Blog")

<div class="jumbotron">
    <h1>Search Blog</h1>
</div>

<form name="frmSearchBlog" action="/search_blog" method="post">
    <table class="table">
        <tr>
            <td class="col-md-2">Title:</td>
            <td class="col-md-2"><input type="text" name="txtTitle"class="form-control"></td>
        </tr>
        <tr>
            <td class="col-md-2">Content:</td>
            <td class="col-md-2"><input type="text" name="txtContent" class="form-control"></td>
        <tr>
            <td class="col-md-2">Tags:</td>
            <td class="col-md-2"><input type="text" name="txtTag" class="form-control"></td>
        </tr>
        <tr>
            <td class="col-md-2"></td></a>
            <td class="col-md-2">
                <input class="btn btn-primary" type="submit" value="Submit">
                <a class="btn btn-primary" href="/" role="button">Back</a>
            </td>
        </tr>
    </table>
</form>

	% if blogs != [] :
		<table class="table">
			<tr>
				<th>Title</th>
				<th>Date</th>
				<th>Text</th>
				<th>Tags</th>
			</tr>
			% for b in blogs:
			<tr>
				<td>{{b["post_title"]}}</td>
				<td>{{b["post_date"]}}</td>
				<td>{{b["post_text"]}}</td>
				<td>
				{{b["post_tags"]}}
				</td>
				<td>
					<a href="/find/{{b['_id']}}" class="btn btn-info" role="button">Edit</a>
					<a href="/delete/{{b['_id']}}" class="btn btn-info delete" role="button">Delete</a>
				</td>
			</tr>
			% end
		</table>
	% end