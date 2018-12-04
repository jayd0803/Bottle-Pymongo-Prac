% rebase('layout.tpl', title='Home Page')

<div class="jumbotron">
	<h1>Blogs</h1>
</div>

<p><a href="/add">Add a new blog</a></p>

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