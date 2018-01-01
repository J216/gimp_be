echo "New files in art folder in the last 30:"
expr `find $HOME/art/script_drawing/ -cmin -43200 | wc -l` - 1
echo "New files in art folder in the last 7 days:"
expr `find $HOME/art/script_drawing/ -cmin -10080 | wc -l` - 1
echo "New files in art folder in the last 24 hours:"
expr `find $HOMEart/script_drawing/ -cmin -1440 | wc -l` - 1
echo "New files in art folder in the last 12 hours:"
expr `find $HOME/art/script_drawing/ -cmin -720 | wc -l` - 1
echo "New files in art folder in the last hour:"
expr `find $HOME/art/script_drawing/ -cmin -60 | wc -l` - 1
echo "New files in art folder in the last 20 minutes:"
expr `find $HOME/art/script_drawing/ -cmin -20 | wc -l` - 1
echo "New files in art folder in the last 10 minutes:"
expr `find $HOME/art/script_drawing/ -cmin -10 | wc -l` - 1
echo "New files in art folder in the last minute:"
expr `find $HOME/art/script_drawing/ -cmin -1 | wc -l` - 1
